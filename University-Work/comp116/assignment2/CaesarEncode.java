/**
 * A program that uses the CaesarCipher to encode text
 *
 * @author Patrick Totzke
 */
public class CaesarEncode{

   public static void main (String args[]){
       int key = 3;
       String text = "";

       // parse command line parameters
       // Check if there are exactly two parameters
       if (args.length > 2) endEarly("Too many parameters!");
       if (args.length < 2) endEarly("Too few parameters!");
       
       // interpret the first one as integer
       try{
           text = args[1];
           key = Integer.parseInt(args[0]);
       }
       catch (NumberFormatException e) {
           endEarly("Could not parse first parameter (n) as int");
       }
       
       // instantiate a CaesarCipher and use it
       Cipher cc = new CaesarCipher(key);
       System.out.println(cc.encrypt(text));

   }
   
   /** print message and usage help and terminate unsuccessfully */
   public static void endEarly(String message){
       System.out.println(message);
       System.out.println("Usage: java CaesarEncode n \"cipher text\"");
       System.exit(-1);
   }
}
