"""MCP Server for Simulated Annealing Combinatorial Optimizer Skill."""
import json
import sys
from client import SimulatedAnnealingOptimizer

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "optimize_tsp",
                            "description": "Optimize Traveling Salesperson Problem via Simulated Annealing",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "coordinates": {
                                        "type": "array",
                                        "items": {"type": "array", "items": {"type": "number"}}
                                    },
                                    "initial_temp": {"type": "number"},
                                    "cooling_rate": {"type": "number"},
                                    "max_iterations": {"type": "integer"}
                                },
                                "required": ["coordinates"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                coords = [tuple(c) for c in args["coordinates"]]
                solver = SimulatedAnnealingOptimizer(
                    initial_temp=args.get("initial_temp", 100.0),
                    cooling_rate=args.get("cooling_rate", 0.995),
                    max_iterations=args.get("max_iterations", 5000)
                )
                output = solver.optimize_tsp(coords)
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(output)}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
