import unittest

# Discover and run all tests in the current directory and subdirectories
loader = unittest.TestLoader()
suite = loader.discover(start_dir='.', pattern='test_*.py')

runner = unittest.TextTestRunner()
result = runner.run(suite)

# Print summary
print(f"Ran {result.testsRun} tests.")
if result.wasSuccessful():
    print("All tests passed successfully.")
else:
    print(f"Errors: {len(result.errors)}")
    print(f"Failures: {len(result.failures)}")

# Print detailed errors and failures
for test, err in result.errors:
    print(f"Error in {test}: {err}")
for test, fail in result.failures:
    print(f"Failure in {test}: {fail}")