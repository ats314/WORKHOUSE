param([switch]$Apply)
$ErrorActionPreference = 'Stop'
$auditRoot = $PSScriptRoot
$planPath = Join-Path $auditRoot 'QUARANTINE_PLAN.json'
$plan = Get-Content -LiteralPath $planPath -Raw | ConvertFrom-Json
$taskRoot = [IO.Path]::GetFullPath($plan.root).TrimEnd('\')
$taskPrefix = $taskRoot + '\'
$quarantineRoot = Join-Path $taskRoot 'quarantine/2026-09-07-exact-duplicates'
$checked = @()
foreach ($entry in $plan.moves) {
    $sourcePath = [IO.Path]::GetFullPath((Join-Path $taskRoot $entry.original_path))
    $destinationPath = [IO.Path]::GetFullPath((Join-Path $taskRoot $entry.quarantine_path))
    $retainedPath = [IO.Path]::GetFullPath((Join-Path $taskRoot $entry.retained_path))
    foreach ($candidatePath in @($sourcePath, $destinationPath, $retainedPath)) {
        if (-not $candidatePath.StartsWith($taskPrefix, [StringComparison]::OrdinalIgnoreCase)) {
            throw "Path leaves explicitly authorized C:\WORKHOUSE: $candidatePath"
        }
    }
    if (-not $destinationPath.StartsWith($quarantineRoot + '\', [StringComparison]::OrdinalIgnoreCase)) {
        throw "Destination leaves the checked quarantine directory: $destinationPath"
    }
    if ($entry.original_path -match '(?i)^WORKHOUSE-autonomous|^ALL THEORY/WORKHOUSE(?:-w98)?/|(?:^|/)\.git/') {
        throw "Cannot move repository evidence: $sourcePath"
    }
    if ((Test-Path -LiteralPath $destinationPath)) { throw "Destination already exists: $destinationPath" }
    foreach ($candidatePath in @($sourcePath, $retainedPath)) {
        $item = Get-Item -LiteralPath $candidatePath
        if ($item.PSIsContainer -or $item.LinkType) { throw "Expected regular file: $candidatePath" }
        if ((Get-FileHash -LiteralPath $candidatePath -Algorithm SHA256).Hash.ToLowerInvariant() -ne $entry.sha256) {
            throw "Content changed after reviewed plan: $candidatePath"
        }
    }
    $checked += [pscustomobject]@{ entry = $entry; source = $sourcePath; destination = $destinationPath; retained = $retainedPath }
}
if (-not $Apply) {
    [pscustomobject]@{ preflight = 'passed'; files = $checked.Count; moved = 0 } | ConvertTo-Json
    exit 0
}
if (Test-Path -LiteralPath $quarantineRoot) { throw 'Quarantine batch already exists; inspect its journal before retrying.' }
[IO.Directory]::CreateDirectory($quarantineRoot) | Out-Null
Copy-Item -LiteralPath $planPath -Destination (Join-Path $quarantineRoot 'MANIFEST.json')
$journalPath = Join-Path $quarantineRoot 'MOVES.jsonl'
foreach ($checkedEntry in $checked) {
    [IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($checkedEntry.destination)) | Out-Null
    Move-Item -LiteralPath $checkedEntry.source -Destination $checkedEntry.destination
    if (Test-Path -LiteralPath $checkedEntry.source) { throw 'Move left the original path present.' }
    foreach ($candidatePath in @($checkedEntry.destination, $checkedEntry.retained)) {
        if ((Get-FileHash -LiteralPath $candidatePath -Algorithm SHA256).Hash.ToLowerInvariant() -ne $checkedEntry.entry.sha256) {
            throw "Post-move digest mismatch: $candidatePath"
        }
    }
    $journalRow = [ordered]@{ original_path = $checkedEntry.entry.original_path; quarantine_path = $checkedEntry.entry.quarantine_path; retained_path = $checkedEntry.entry.retained_path; sha256 = $checkedEntry.entry.sha256; verified = $true }
    Add-Content -LiteralPath $journalPath -Value ($journalRow | ConvertTo-Json -Compress) -Encoding utf8
}
[pscustomobject]@{ moved = $checked.Count; verified = $checked.Count; deleted = 0; manifest = (Join-Path $quarantineRoot 'MANIFEST.json') } | ConvertTo-Json
