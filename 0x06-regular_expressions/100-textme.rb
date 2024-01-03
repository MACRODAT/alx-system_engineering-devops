#!/usr/bin/env ruby

fm = ARGV[0].scan(/fm:(.*?)\]/)
to = ARGV[0].scan(/to:(.*?)\]/)
fg = ARGV[0].scan(/fg:(.*?)\]/)
puts [fm, to, fg].join(',')
