"""
Entry point for CyberGuardian demo pipeline.
Run: python run.py --demo sample_data/alert_sample.txt
"""
import argparse
from agents.supervisor_agent import Supervisor

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--demo', help='Path to demo alert text file', required=False)
    args = parser.parse_args()

    sup = Supervisor()
    if args.demo:
        try:
            with open(args.demo, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print('Demo file not found:', args.demo)
            return
        report = sup.run_pipeline(content)
        print('\n--- Generated Incident Report (markdown) ---\n')
        print(report)
        print('\nReport saved to reports/ folder (if pdf conversion available, a PDF may be created).')
    else:
        print('No demo provided. You can run `python run.py --demo sample_data/alert_sample.txt`')

if __name__ == '__main__':
    main()