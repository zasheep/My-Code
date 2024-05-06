/**
 * A program that is used to encrypt a given text using the CaesarCipher Method
 *
 * @author Zariff Aminuddin
 * @version 13.0.2, 2020-01-14
 *
 */
public class CaesarCipher extends RotationCipher implements Cipher{
	
	int num;
	
	/**
	 * A key is kept within the method for later used
	 */
	public CaesarCipher(int key){
		super(key);
		num = key;
	}
	
	/**
	 * Returns an encrypt version of a given text, encrypted by a given shift key
	 *
	 * @param shift	the shift/key
	 * @param text the english text
	 * @return String the encrypted text 
	 */
	public String rotate(int shift, String text){
		StringBuilder result = new StringBuilder();
		
		while ((shift < 0)||(shift > 26)){ //Corrects the shift to the correct number if out of range (0-26)
			if (shift < 0){
				shift = shift + 26;
			}
			else if (shift > 26){
				shift = shift - 26;
			}
		}
		
		for (char character : text.toCharArray()) {
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
            else if(character >= 'A' && character <= 'Z') {
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
		String s = result.toString();
		return s;
	}
	
	/**
	 * Interface methods utilising the encryption only   
	 *
	 * @param plainText english text is given
	 * @return String encrypted text 
	 */
	public String encrypt(String plainText){
		String s = rotate(num, plainText);
		return s;
	}
	
	
	public String decrypt(String cipherText){
		return cipherText;
	}

}

