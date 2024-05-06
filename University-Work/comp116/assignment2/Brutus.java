/**
 * A program that is used to decrypt an encryption using ChiSquared values
 *
 * @author Zariff Aminuddin
 * @version 13.0.2, 2020-01-14
 *
 */
public class Brutus implements Cipher{
	
	public Brutus(){
	}
	
	double[] knownFreq = {0.0855, 0.0160, 0.0316, 0.0387, 0.1210,
						0.0218, 0.0209, 0.0496, 0.0733, 0.0022,
						0.0081, 0.0421, 0.0253, 0.0717, 0.0747,
						0.0207, 0.0010, 0.0633, 0.0673, 0.0894,
						0.0268, 0.0106, 0.0183, 0.0019, 0.0172,
						0.0011};
						
	/**
	 * 
	 * Computes the frequency of each letter of a string
	 * 
	 * @param text given string to calculate
	 * @return double[] an array listing each letters frequency in alphabetical order
	 */
	private double[] computeFrequencies(String text){
		double[] array = new double[26];
		double probability = 0;
		char character = 'a';
		double size = 0;
		
		text = text.toLowerCase(); //changes the text to lower cases so we dont have to deal with upper cases
		
		for (char element : text.toCharArray()){ 	//this for loop is to count how many letters are in the text without counting up spaces, etc.
			if (element >= 'a' && element <= 'z'){
				size = size + 1;
			}
		}
		
		for (int i = 0; i < array.length; i++) {  //nested for loop to repeat for each letter in the alphabet
			for (char element : text.toCharArray()){ //for loop to count out how many letters are repeated.
				if (element == character){
					probability = probability+1; 
				} else {
					probability = probability;
				}
			}
			probability = (probability/size);
			array[i] = probability; 	//assigns the probability of the letter in their spot of the alphabet
			probability = 0;
			character = (char)  (character + 1); //moves onto the next character, eg from a -> b.
		}
		
		return array;
	}
	
	/**
	 *
	 * Computes the summation of ChiSquare Values for each letter
	 *
	 * @param freqsA known frequencies of english letters, the other is  
	 * @param freqsB the frequency of english letters in a given text
	 * @return double the sum of all ChiSquare letter values
	 */
	private double chiSquared(double[] freqsA, double[] freqsB){ //calculates each letter's ChiSquared value and sums them up 
		double num;
		double sum = 0;
	
		for (int i = 0; i < freqsA.length; i++){ 
			num = (Math.pow((freqsA[i] - freqsB[i]), 2))/freqsB[i];
			sum = sum + num;
		}
		
		return sum;
	}
	
	/**
	 *
	 * Interface method 1
	 *
	 * @param plainText the encrypted text
	 * @return String the encrypted text
	 */
	public String encrypt(String plainText){ 
		return plainText;
	}
	
	/**
	 *
	 * Interface method 2
	 *
	 * @param cipherText the encrypted text
	 * @return String the text decrypted into english
	 */
	public String decrypt(String cipherText){		
		StringBuilder result = new StringBuilder(); //initialises an array of Strings
		String Decrypt = "";
		double LowestChiSquare = Math.pow(10,6); //value is really high in case of very large cipherText results in a large number
		
		for (int shift = 0; shift < 26; shift++){ //for loop checks for every possible shift of the Cipher
			for (char character : cipherText.toCharArray()){ //uses similar code from rotate() to apply shift translation to the Cipher
				if(character >= 'a' && character <= 'z'){
					character = (char) (character + shift);
					// if shift alphabet greater than 'z'
					if(character > 'z') {
						// reshift to starting position 
						character = (char) (character+'a'-'z'-1);
					}
					result.append(character);
				}
				
				// if alphabet lies between 'A'and 'Z'
				else if(character >= 'A' && character <= 'Z'){
					character = (char) (character + shift);
					// if shift alphabet greater than 'Z'
						if(character > 'Z') {
						//reshift to starting position 
							character = (char) (character+'A'-'Z'-1);
						}
					result.append(character);
				}
				
				else {
					result.append(character);  
				}
			}			
			
			String s = result.toString(); //Converts the Stringbuilder array into a useable String
			double[] frequencies = computeFrequencies(s); 
			
			for (int i = 0; i<frequencies.length; i++){ //for loop here is to calculate the String's ChiSquared value and takes the lowest from possible shift translations
				double num = chiSquared(frequencies, knownFreq);
				if (LowestChiSquare > num){
					LowestChiSquare = num;
					Decrypt = s;
				} else {
					LowestChiSquare = LowestChiSquare;
				}
			}
			result.delete(0, result.length()); //Empties out my Result/StringBuilder so it doesn't append endlessly into a very long string
		}
		return Decrypt;
		
	}
	
	//main is copied from the CaesaeEncode.java file provided and was modified to fit Brutus.java
	public static void main (String args[]){
        String text = "";
		
        if (args.length > 1) endEarly("Too many parameters!");
        if (args.length < 1) endEarly("Too few parameters!");
         
        try{
            text = args[0];
        }
        catch (NumberFormatException e) {
           endEarly("Could not parse first parameter (n) as int");
        }
	
        Cipher cc = new Brutus();
        System.out.println(cc.decrypt(text));
    }
   
    /** print message and usage help and terminate unsuccessfully */
    public static void endEarly(String message){
        System.out.println(message);
        System.out.println("Usage: java CaesarEncode n \"cipher text\"");
        System.exit(-1);
    }
	
}
	