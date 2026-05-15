public class arrays1 {
    public static void main(String[] args) {
        int  [] Claudio = new int [10];

        System.out.printf("%s%8s%n", "Index", "Value");
        
        for (int counter = 0; counter < Claudio.length; counter++) {
           
            System.out.printf("%5d%8d%n", counter, Claudio[counter]);
        }
    }
    
}
