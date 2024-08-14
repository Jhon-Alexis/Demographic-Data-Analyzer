import unittest
import demographic_data_analyzer
class DemographicDataAnalyzerTestCase(unittest.TestCase):

    def setUp(self):
        self.data = demographic_data_analyzer.calculate_demographic_data(print_data=False)

    def test_race_count(self):
        actual = self.data["race_count"].tolist()
        expected = [27816, 3124, 1039, 311, 271]
        self.assertAlmostEqual(actual,expected,"Expected values [27816, 3124, 1039, 311, 271]")

    def test_avg_men(self):
        actual = self.data["avg_men"]
        expected = 39.43
        self.assertAlmostEqual(actual,expected,"Expected different value for average age of men.")

    def test_per_bac(self):
        actual = self.data["per_bac"]
        expected = 16.45
        self.assertAlmostEqual(actual,expected,"Expected different value for percentage of people who have a Bachelor's degree.")
    
    def test_per_ae(self):
        actual = self.data["per_bmd_m50"]
        expected = 46.54
        self.assertAlmostEqual(actual, expected,"Expected different value for percentage of people with advanced education that make more than 50K")

    def test_per_wo(self):
        actual = self.data["per_wo_ae_m50"]
        expected = 17.37
        self.assertAlmostEqual(actual, expected,"Expected different value for percentage of people without advanced education make more than 50K" )
    
    def test_min_hour(self):
        actual = self.data["min_hours"]
        expected = 1
        self.assertAlmostEqual(actual, expected, "Expected different value for the minimum number of hours a person works per week ")
        
    def test_per_min_50(self):
        actual = self.data["per_min_50"]
        expected = 10.0
        self.assertAlmostEqual(actual,expected, "Expected different value for percentage of the people who work the minimum number of hours per week have a salary of more than 50K")

    def test_country_high_per(self):
        actual = self.data["high_earn_per"]
        expected = 91.46
        self.assertAlmostEqual(actual,expected, "Expected different value for percentage of country with the highest percentage of people that earn >50K")

    def test_country_high(self):
        actual = self.data["high_earn_country"]
        expected = 'United-States'
        self.assertEqual(actual,expected, "Expected different value for country with the highest percentage of people that earn >50K")

    def test_country_top(self):
        actual = self.data["occ_top"]
        expected = "Prof-specialty"
        self.assertEqual(actual,expected, "Expected different value for the most popular occupation in India")

if __name__ == "__main__":
    unittest.main()