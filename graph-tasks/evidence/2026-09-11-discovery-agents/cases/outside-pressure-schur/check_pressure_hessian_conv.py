import sys; sys.argv=['x']
exec(open(sys.path[0]+'/check_pressure_hessian.py').read().split('run(0.8, 1.5, 0.6, 2.0, 0.0)')[0])
for N in (161, 241, 321):
    run(0.8, 1.5, 0.6, 2.0, 0.15, N=N)
