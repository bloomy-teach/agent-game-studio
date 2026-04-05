import logging
import sys
from workflow import GameWorkflow
                                                
# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    try:
        logging.info('Starting the game workflow...')
        workflow = GameWorkflow()
        workflow.run()  # Assuming the run method handles the complete workflow
        logging.info('Workflow completed successfully.')
        results = workflow.results  # Retrieve the results in a user-friendly format
        display_results(results)
    except Exception as e:
        logging.error(f'An error occurred: {str(e)}')
        sys.exit(1)  # Exit code 1 for errors

def display_results(results):
    if not results:
        logging.warning('No results to display.')
        return
    logging.info('Displaying results...')
    for key, value in results.items():
        print(f'{key}: {value}')  # Format results in a user-friendly way

if __name__ == '__main__':
    main()