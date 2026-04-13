import sys
import os

# Add parent directory to path to import sigma_atp
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sigma_atp import SigmaATPMonitor

def main():
    # 1. Initialize the Metabolic Tracker
    monitor = SigmaATPMonitor(project_name="CommunityTest")

    print("[*] Simulating AI Metabolic Cycle...")
    
    # 2. Simulate an Action
    prompt = "Design a sovereign energy system based on photosynthesis."
    response = "The system would use high-efficiency solar cells as digital chloroplasts..."
    
    # 3. Log the ATP expenditure
    cycle = monitor.log_metabolism(prompt, response, tag="conceptual_research")
    
    print(f"[+] ATP Expended in this cycle: {cycle['in_atp'] + cycle['out_atp']} tokens.")
    
    # 4. Generate Report
    report = monitor.get_atp_report()
    print("\n--- METABOLIC REPORT ---")
    for key, value in report.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
