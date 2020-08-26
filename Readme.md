System Requirement:
	Python 3
	
To Run:

	Traverse to the Directory where the Main Task and Test script are cloned/copied. Execute the commands below to run the Scripts.
	
	For Linux:
		python3 test_ThinkBridge_task.py 				python3 ThinkBridge_task.py
		
	For Windows:
		python test_ThinkBridge_task.py 				python ThinkBridge_task.py
		
	** In order to run the TestScript it should be in same directory as ThinkBridge_task.py
		

To Configure Test Scripts:
		
	Test Cases are stored in Cases Dict with input as the Key and Output as the value Pair
	
		Cases key ->Input
		Cases[key] -> Expected Output
		
	Default Test Cases:
		"123456.78":"one lakh twenty three thousand four hundred fifty six Rs seventy eight paise","-98":"Number not in range 0-1000000, Try in valid range","9653.ww":"Number Contains Character, Hence cannot be converted",".67":"sixty seven paise",".6":"sixty  paise","123":"one hundred twenty three Rs","sasfg":"Number Contains Character, Hence cannot be converted","09876.5":"nine thousand eight hundred seventy six Rs fifty  paise"