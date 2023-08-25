set Browser=chrome

behave -f allure -o Report\allure_result -f html -o Report\behave-report.html -D browser=%Browser%


::behave @rerun_failing.feature
::python Utility/generate_allure_report.py
::python Utility/send_mail.py %Browser%
