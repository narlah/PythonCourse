def num_ways_X_bottom_up(n, stepsPossible):
    """Example for a dynamic programming, finally got one algorithm that plagued my thinking for a while   https://youtu.be/5o-kdjv7FD0?t=1139  """
    if n == 0:
        return 1
    nums = (n + 1) * [0]
    nums[0] = 1
    for i in range(1, n + 1):
        total = 0
        for j in stepsPossible:
            if i - j >= 0:
                total += nums[i - j]
        nums[i] = total
    return nums[n]


print(num_ways_X_bottom_up(4, {2, 3}))


""" 
public class Str237 {
    static int str237(String S) {
        int[] D = new int[238];
        D[0] = 1;
        for (int i = 0; i < S.length(); i++) {
            int c = S.charAt(i);
            for (int x = 238; x > c;) {
                x--;
                D[x] += D[x - c];
            }
        }
        return D[237];
    }
    public static void main(String[] args) {
        System.out.println(str237("Hello world!"));// 1
        System.out.println(str237("Hello world!!"));// 2
    }
}

Разгледах го мръсника - озползва факта като гледа назад докъде мойе да докара 1-цата като я събира към отместването  което е стоиноста на текущата стоиност

сложноста е пак 0^2
    static int str237(String S) {
        int[] D = new int[238];
        D[0] = 1;
        for (int i = 0; i < S.length(); i++) {
            int c = S.charAt(i);
            for (int x = 237; x >= c; x--) {
                D[x] += D[x - c];
            }
        }
        return D[237];
    }

               
и тука мисленето е ж друга посока - не е да се направят всичките подмножества които дават сума N  а колко колко от числата могат да доведат до сума N
и е лакомо за памет

               

public class StrSubsum {

    static int strSubsum(String S, int sum) {

        int[] D = new int[sum+1];

        D[0] = 1;

        for (int i = 0; i < S.length(); i++) {

            int c = S.charAt(i);

            for (int x = sum; x >= c; x--) {

                D[x] += D[x - c];
            }
        }
        return D[sum];
    }

    public static void main(String[] args) {
        System.out.println(strSubsum("Hello world!",237));// 1
        System.out.println(strSubsum("Hello world!!",237));// 2
    }
}           

"""