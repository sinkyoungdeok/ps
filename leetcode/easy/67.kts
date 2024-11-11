class Solution {
    fun addBinary(a: String, b: String): String {
        val reverseA = a.reversed()
        val reverseB = b.reversed()

        val lenA = a.length
        val lenB = b.length

        val lenMin = if(lenA < lenB) lenA else lenB

        var carry = 0
        var res = ""
        for (i in 0..lenMin-1) {
            val sum = reverseA[i].toString().toInt() + reverseB[i].toString().toInt() + carry

            carry = sum / 2
            res += (sum % 2).toString()
        }

        if (lenA == lenMin) {
            for (i in lenMin..lenB-1) {
                val sum = reverseB[i].toString().toInt() + carry

                carry = sum / 2
                res += (sum % 2).toString()
            }

            println("res: $res, carry: $carry")
        } else {
            for (i in lenMin..lenA-1) {
                val sum = reverseA[i].toString().toInt() + carry

                carry = sum / 2
                res += (sum % 2).toString()
            }

            println("res: $res, carry: $carry")
        }

        if (carry > 0) {
            println("carry: $carry")
            res += "1"
        }

        return res.reversed()
    }
}