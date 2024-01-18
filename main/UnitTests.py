import unittest
from __init__ import *

log_file = "sampleFile.txt"

class TestStringMethods(unittest.TestCase):

    def test_count_logs(self):
        test_count = count_logs(log_file)
        expected = {'INFO': 7, 'DEBUG': 4, 'ERROR': 2}
        self.assertDictEqual(test_count, expected)

    def test_avg_logs(self):
        test_count = avg(calculate_average_run_time(log_file))
        expected = {'BackendApp': 17.25, 'API': 18.666666666666668}
        self.assertDictEqual(test_count, expected)

    def test_errors_app_daily(self):
        test_count = errors_app_daily(log_file)
        expected = 13
        self.assertEqual(test_count, expected)

    def test_most_failed_runs(self):
        test_count = most_failed_runs(log_file)
        expected = ('BackendApp', 1)
        self.assertTupleEqual(test_count, expected)

    def test_most_succesful_runs(self):
        test_count = most_succesful_runs(log_file)
        expected = ('BackendApp', 4)
        self.assertTupleEqual(test_count, expected)

    def test_count_errors_by_third_of_day(self):
        test_count = count_errors_by_third_of_day(log_file)
        expected = "00:00:00 - 07:59:59"
        self.assertEqual(test_count, expected)

    def test_calculate_run_times(self):
        test_count = calculate_run_times(log_file)
        expected = {'BackendApp': {'shortest': ('02:51:24', 15), 'longest': ('13:08:50', 20)},
                    'API': {'shortest': ('17:23:35', 14), 'longest': ('03:42:50', 22)}}
        self.assertDictEqual(test_count, expected)

    def test_count_activities_by_hour(self):
        test_count = count_activities_by_hour(log_file)
        expected = {'FrontendApp': 8, 'BackendApp': 1, 'API': 17}
        self.assertDictEqual(test_count, expected)

    def test_calculate_failure_rates(self):
        test_count = calculate_failure_rates(log_file)
        expected = {'FrontendApp': 0.0, 'BackendApp': 11.11, 'API': 12.5, 'SYSTEM': 0.0}
        self.assertDictEqual(test_count, expected)

if __name__ == '__init__':
    unittest.main()
