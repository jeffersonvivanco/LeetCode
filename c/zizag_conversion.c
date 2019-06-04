#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
 * Zizag Conversion Solution
 * @author: Jefferson Vivanco
 * @summary: Calculate 3 intervals: top/bottom, other_1, other_2. Traverse
 * the first numRows letters of the string you want to convert. As you traverse
 * append the letter to a new string and if it's the first letter or numRows 
 * letter use top/bottom interval to jump to the other char in the string 
 * and append it to the new string. After you traverse all the letters, you'll
 * have the final output.
 * @notes: Wrote a small function assertEquals() that checks if expected converted string
 * equals what the function computed.
 * */

char* convert(char *s, int num_rows);
void assertEquals(char *expected, char *actually);

char *temp;

int main() {
	
	char* c = convert("PAYPALISHIRING", 3); // len is 14
	assertEquals("PAHNAPLSIIGYIR", c);
	free(c);
	
	char* c6 = convert("PAYPALISHIRING", 4); 
	assertEquals("PINALSIGYAHRPI", c6);
	free(c6);
	
	char* c7 = convert("PAYPALISHIRING", 5);
	assertEquals("PHASIYIRPLIGAN", c7);
	free(c7);
	
	
	char* c2 = convert("ABC", 3);
	assertEquals("ABC", c2);
	//free(c2); // don't need to free since we didn't use malloc
	
	
	char* c3 = convert("ABCDEF", 3);
	assertEquals("AEBDFC", c3);
	free(c3);
	
	char *c5 = convert("JEFFISAPROGRAMMERPERIOD", 4);
	assertEquals("JAAEESPRMPRFIRGMRIDFOEO", c5);
	
	char *c8 = convert("AB", 1);
	assertEquals("AB", c8);
	        
}

char* convert(char *s, int numRows){
	
	int i, len = (int)strlen(s), index = 0;
	
	if (len == numRows || numRows == 1) return s; // if its same size, return
	
	int top_bottom_interval = (numRows * 2) - 2;
	
	int other_interval_1 = top_bottom_interval - 2, other_interval_2 = 2;
	
	char *c = malloc(sizeof(char) * (len + 1)); // adding 1 to length to make room for null char
	if (c == NULL){
		printf("[Error] malloc error, returning NULL");
	}
	char *converted_string = c;

	int other_interval_index = 1; // used to decide whether to use other_interval_1 or 2
	
	for (i = 0; i < numRows; i++){
		if (i == 0 || i == numRows - 1) { // deals with top and bottom intervals
			index = i;
			while (index < len){
				*converted_string++ = s[index];
				index += top_bottom_interval;
				
			}
		} else { // deals with other intervals
			index = i;
			other_interval_index = 1;
			while (index < len){
				*converted_string++ = s[index];
				if (other_interval_index % 2 != 0){ // time to increment by other_interval_1
					index += other_interval_1;
				} else {
					index += other_interval_2;
				}
				other_interval_index++;
			}
			other_interval_1 -= 2; // decrementing by two look at algorithm at top
			other_interval_2 += 2; // incrementing by two look at algorithm at top
		}
	}
	
	*converted_string = '\0';
	
    return c;
}

void assertEquals(char *expected, char *actually){
	int c_comp = strcmp(expected, actually);
	printf("\n[Test] Expected: --%s-- Actual: --%s-- Result: --%s--\n", expected, actually, c_comp == 0 ? "Passed" : "Failed");
}
