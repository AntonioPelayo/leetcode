"""Antonio Pelayo April 11, 2020
Problem: 1410 HTML Entity Parse
Difficulty: Medium

HTML entity parser is the parser that takes HTML code as input and replace all 
the entities of the special characters by the characters itself.

The special characters and their entities for HTML are:

Quotation Mark: the entity is &quot; and symbol character is ".
Single Quote Mark: the entity is &apos; and symbol character is '.
Ampersand: the entity is &amp; and symbol character is &.
Greater Than Sign: the entity is &gt; and symbol character is >.
Less Than Sign: the entity is &lt; and symbol character is <.
Slash: the entity is &frasl; and symbol character is /.
Given the input text string to the HTML parser, you have to implement the entity parser.

Return the text after replacing the entities by the special characters.

Example 1:
Input: text = "&amp; is an HTML entity but &ambassador; is not."
Output: "& is an HTML entity but &ambassador; is not."
Explanation: The parser will replace the &amp; entity by &

Example 2:
Input: text = "and I quote: &quot;...&quot;"
Output: "and I quote: \"...\""

Example 3:
Input: text = "Stay home! Practice on Leetcode :)"
Output: "Stay home! Practice on Leetcode :)"

Example 4:
Input: text = "x &gt; y &amp;&amp; x &lt; y is always false"
Output: "x > y && x < y is always false"

Example 5:
Input: text = "leetcode.com&frasl;problemset&frasl;all"
Output: "leetcode.com/problemset/all"

Constraints:
1 <= text.length <= 10^5
The string may contain any possible characters out of all the 256 ASCII characters.
"""

def entityParser(text):
    ans = ''
    replacements = {'&quot;': '\"', '&apos;': "'", '&amp;': '&',
                    '&gt;': '>',    '&lt;': '<',   '&frasl;': '/'}
        
    # Iterate through all chars in text
    i = 0
    while i < len(text):
        command = ''
        if text[i] == '&':    # Catch start of command
            while text[i] != ';':
                command += text[i]
                i += 1
            command += ';'    # End of command
            i += 1

            # Check for valid command
            if command in replacements:
                ans += replacements[command]  # Append replacement to answer
            else:
                ans += command                # Append invalid command 
                    
        else:
            ans += text[i]                    # Append all other chars
            i += 1
                    
    return ans

a = "&amp; is an HTML entity but &ambassador; is not."
b = "and I quote: &quot;...&quot;"
c = "Stay home! Practice on Leetcode :)"
d = "x &gt; y &amp;&amp; x &lt; y is always false"
e = "leetcode.com&frasl;problemset&frasl;all"
 
print(entityParser(a))
print(entityParser(b))
print(entityParser(c))
print(entityParser(d))
print(entityParser(e))