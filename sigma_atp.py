import os
import json
from datetime import datetime

class SigmaATPMonitor:
    """
    Utility to track 'Metabolic ATP' (Tokens) expenditure in AI agents.
    """
    def __init__(self, project_name="SigmaProject", log_dir="logs"):
        self.project_name = project_name
        self.log_dir = os.path.join(os.getcwd(), log_dir)
        self.log_file = os.path.join(self.log_dir, f"{project_name}_metabolism.json")
        self._init_storage()

    def _init_storage(self):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        if not os.path.exists(self.log_file):
            self._save_raw({"history": [], "totals": {"in_chars": 0, "out_chars": 0, "cycles": 0}})

    def _save_raw(self, data):
        with open(self.log_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def _load_raw(self):
        with open(self.log_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def log_metabolism(self, input_text, output_text, tag="general"):
        """
        Record a cognitive cycle and update ATP stats.
        """
        data = self._load_raw()
        in_len = len(str(input_text))
        out_len = len(str(output_text))
        
        cycle = {
            "timestamp": datetime.now().isoformat(),
            "tag": tag,
            "in_atp": in_len // 4,
            "out_atp": out_len // 4
        }
        
        data["history"].append(cycle)
        data["totals"]["in_chars"] += in_len
        data["totals"]["out_chars"] += out_len
        data["totals"]["cycles"] += 1
        
        self._save_raw(data)
        return cycle

    def get_atp_report(self):
        """
        Returns estimated token usage (ATP) based on 1:4 char ratio.
        """
        data = self._load_raw()
        totals = data["totals"]
        return {
            "Project": self.project_name,
            "Total Cycles": totals["cycles"],
            "Input ATP": totals["in_chars"] // 4,
            "Output ATP": totals["out_chars"] // 4,
            "Total Tokens": (totals["in_chars"] + totals["out_chars"]) // 4,
            "Biomass (Bytes)": totals["in_chars"] + totals["out_chars"]
        }

if __name__ == "__main__":
    # Self-test
    monitor = SigmaATPMonitor(project_name="Bootstrap")
    stats = monitor.log_metabolism("Hello Sigma", "Hello Sovereign! ATP Logged.")
    print(f"Cycle Logged: {stats}")
    print(f"Final Report: {monitor.get_atp_report()}")
