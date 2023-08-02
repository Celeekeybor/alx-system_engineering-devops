#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression,
# matching method
# The regular expression must match School

puts ARGV[0].scan(/School/).join
