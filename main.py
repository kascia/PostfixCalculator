from mysolver import Solver
from myio import IO

if __name__ == "__main__":
    io = IO()
    solver = Solver()

    infix = io.get_infix()
    ans = solver.solve(infix)
    
    io.print_ans(ans)
    
    