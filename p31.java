package com.company;

import java.util.Scanner;
/**
 * Created by xueyishu on 6/18/15.
 */
public class coucoin {

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int amount = input.nextInt();
        int isExit = 0;
        int counter = 0;
        OUT:
        for (int one = 0; one <= amount; ++one) {
            for (int two = 0; two <= amount / 2; ++two) {
                for (int five = 0; five <= amount / 5; ++five) {
                    for (int ten = 0; ten <= amount / 10; ++ten) {
                        for (int twenty = 0; twenty <= amount / 20; ++twenty) {
                            for (int fifty = 0; fifty <= amount/50; ++fifty) {
                                for (int p100 = 0; p100 <= amount/100; ++p100) {
                                    for (int p200 = 0; p200 <= amount/200; ++p200) {
                                        if (one + two * 2 + five * 5 + ten * 10 + twenty * 20 + fifty*50 + p100*100 + p200*200 == amount) {
                                            counter += 1;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        System.out.println(counter);
    }
}
