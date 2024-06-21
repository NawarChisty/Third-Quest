#!/bin/bash

# Run the JMeter test
jmeter -n -t API_Performance_Test.jmx -l test_results.jtl

# Check if the test passed
# Assuming we are looking for errors and duration issues
if grep -q "false" test_results.jtl; then
    echo "Performance test failed: response time exceeded 1 second or other errors."
    exit 1
else
    echo "Performance test passed."
    exit 0
fi
