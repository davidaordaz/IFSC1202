def ParseDegreeString(ddmmss):
    degree_pos = ddmmss.find("\u00B0")
    minute_pos = ddmmss.find("'")
    second_pos = ddmmss.find("\"")
    
    degrees = float(ddmmss[:degree_pos])
    minutes = float(ddmmss[degree_pos + 1:minute_pos])
    seconds = float(ddmmss[minute_pos + 1:second_pos])
    
    return degrees, minutes, seconds

def DDMMSStoDecimal(degrees, minutes, seconds):
    return degrees + (minutes / 60) + (seconds / 3600)

input_filename = "TextFiles/07.Project Angles Input.txt"
output_filename = "TextFiles/07.Project Angles Output.txt"

infile = open(input_filename, "r")
outfile = open(output_filename, "w")

count = 0
for line in infile:
    line = line.strip()
    if line:
        degrees, minutes, seconds = ParseDegreeString(line)
        decimal_degree = DDMMSStoDecimal(degrees, minutes, seconds)
        outfile.write(str(decimal_degree) + "\n")
        count += 1

infile.close()
outfile.close()

print(str(count) + " records processed")
