/**
 * A program used for abstract methods
 *
 * @author Zariff Aminuddin
 * @version 13.0.2, 2020-01-14
 *
 */
public abstract class RotationCipher implements Cipher {

	protected abstract String rotate(int shift, String text);
	
	int num;
	
	public RotationCipher(int key){
		num = key;
	} 		

	/**
	 * Interface methods below 
	 *
	 */
	
	public String encrypt(String plainText){
		return plainText;
	}
	
	public String decrypt(String cipherText){
		return cipherText;
	}

}