import java.util.Stack

class Solution {
    fun isValid(s: String): Boolean {
        val st = Stack<Char>()

        for (i in s) {
            if (i == '(' || i == '{' || i == '[') {
                st.push(i)
            } else {
                if (st.isEmpty()) {
                    return false
                }
                if (i == ')') {
                    if (st.peek() == '(') {
                        st.pop()
                    } else {
                        return false
                    }
                } else if (i == '}') {
                    if (st.peek() == '{') {
                        st.pop()
                    } else {
                        return false
                    }
                } else {
                    if (st.peek() == '[') {
                        st.pop()
                    } else {
                        return false
                    }
                }
            }
        }

        if (st.isNotEmpty()) return false

        return true
    }
}