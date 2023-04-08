from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner

# 
import Test002notPhone
import Test003notPassword
import Test004notEmail
import Test005notName
import Test006notClickagree

TC002 = TestLoader().loadTestsFromTestCase(Test002notPhone.testnotPhone)
TC003 = TestLoader().loadTestsFromTestCase(Test003notPassword.testnotPassword)
TC004 = TestLoader().loadTestsFromTestCase(Test004notEmail.testnotEmail)
TC005 = TestLoader().loadTestsFromTestCase(Test005notName.testnotName)
TC006 = TestLoader().loadTestsFromTestCase(Test006notClickagree.testnotClickagree)

listTestcase = [
    TC002,
    TC003,
    TC004,
    TC005,
    TC006,

]
suite = TestSuite(listTestcase)

runner = HTMLTestRunner(report_title="Test Suites Web Registor",output='example_suite',combine_reports=True,report_name="Test Suite Web Registor")

runner.run(suite)