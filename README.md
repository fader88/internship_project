# Careerist Test Automation repository
written in
### Python 3, Behave
https://www.careerist.com/automation


To run the test case and generate Allure report run following in the terminal: behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/subscription_and_payments.feature

To show Allue results run following in the terminal: allure serve test_results/

Run the following prior to "allure serve..." if getting the libawt_xawt.so error: export JAVA_TOOL_OPTIONS="-Djava.awt.headless=true"

