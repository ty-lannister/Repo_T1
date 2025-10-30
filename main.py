ADD NEW BELOW:


SQL Problem:
Tables
visits: Contains columns visitor_id, visit_id, and date.
visitors: Contains columns visitor_id and user_name.
Task: Write a query to:
 - Identify the user with the maximum visits for each day.
 - Resolve ties by choosing the user with the lexicographically smallest name.


python - a list [[1,3],[2,5],[7,9],[8,10]] was given and asked to minimize the range if b >= c where [[a, b],[c, d]]

   A = [[1, 3], [2, 5], [7, 9], [8, 10]]  # List of intervals

out = []   # This will store the merged intervals

i = 0      # Pointer to the "current" interval we're checking
j = 1      # Pointer to the "next" interval

# Loop while there is a 'next' interval to compare
while j < len(A):
    if A[i][1] >= A[j][0]:
        # Overlap: the end of the current interval >= start of the next interval
        # Merge them into the current interval by updating its end to the next interval's end
        A[i] = [A[i][0], A[j][1]]
    else:
        # No overlap: push the current interval into output
        out.append(A[i])
        # Move to the next interval
        i = j
    # Always move to the next interval to compare
    j += 1

# After the loop ends, the last interval hasn't been appended yet — do it now
out.append(A[i])

# Print the final merged intervals
print(out)
