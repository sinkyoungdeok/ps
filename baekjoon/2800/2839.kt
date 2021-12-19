import java.util.*
import kotlin.math.*
 
fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    var maxFive = N / 5

    var res: Int = 100000000

    for (i in 0..maxFive) {
        if( (N - (i*5)) % 3 ==0 ) {
            res = min(res , i + (N-(i * 5)) /3 )
        }
    }

    if (res == 100000000) res = -1

    print(res)

    
}