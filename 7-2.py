# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.



# Desired Output
# Average spam confidence: 0.750718518519

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
value = 0
spam = "X-DSPAM-Confidence:"
#fh = open('mbox-short.txt')
for line in fh:
    if line.startswith(spam) :
        value = value + float(line[line.find(':')+1:].rstrip())
        count = count + 1
    continue
average = value / count
print("Average spam confidence:",average)
