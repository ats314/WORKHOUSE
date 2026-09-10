import Workhouse
import Lean

/- Export the elaborated type and proof dependencies, not identifier matches in
source text. Run through scripts/export_lean_dependencies.py after a strict
`lake build --wfail`. This file adds no mathematical declarations. -/
open Lean Elab Command

run_cmd do
  let env ← getEnv
  for (name, info) in env.constants.toList do
    let spelling := name.toString
    if spelling.startsWith "Workhouse." || spelling.startsWith "_private.Workhouse." then
      let typeDeps := info.type.getUsedConstants.toList.map Name.toString
      let proofDeps := (info.value? true).toList.flatMap fun e =>
        e.getUsedConstants.toList.map Name.toString
      let axioms ← collectAxioms name
      let kind := match info with
        | .thmInfo _ => "theorem"
        | .axiomInfo _ => "axiom"
        | .defnInfo _ => "definition"
        | .opaqueInfo _ => "opaque"
        | .inductInfo _ => "inductive"
        | .ctorInfo _ => "constructor"
        | .recInfo _ => "recursor"
        | .quotInfo _ => "quotient"
      let row := Json.mkObj [
        ("name", toJson spelling), ("kind", toJson kind),
        ("type_dependencies", toJson (typeDeps.mergeSort (· ≤ ·))),
        ("proof_dependencies", toJson (proofDeps.mergeSort (· ≤ ·))),
        ("axioms", toJson (axioms.toList.map Name.toString |>.mergeSort (· ≤ ·)))]
      liftIO <| IO.println ("WORKHOUSE_DEPENDENCY " ++ row.compress)
