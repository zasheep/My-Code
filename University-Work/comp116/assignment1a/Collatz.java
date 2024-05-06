public class Collatz {
	// Methods
	public static int next(int n){
		if (n%2 == 0){
			n = n/2;
			return n;
		}
		else{ 
			n = n*3 + 1;
		return n;
		}
	}
	
	public static int stoppingTime(int n) {
		int count = 1; int iterations = 0;
		String s = "";
		if (n == 1){
			iterations = 0;
		}
		else{
			while (next(n) != 1){
				n = next(n);
				iterations = iterations + 1;
			}
			if (n==2){
			n = next(n);
			iterations = iterations + 1;
			}
			
		}
		count = count + 1;
		n = count;
		return iterations;
	}
	
	public static String sequence(int n, String s) {
		s = n + ", ";
		{return s;}
	}
	
	public static void main(String[] args){
		int n = 1; int count = 1;
		String s = "";
		while (count!=21){
			if (n == 1){
				System.out.println(n);
			}
			else{
				while (next(n) != 1){
					s = sequence(n, s);
					n = next(n);
					System.out.print(s);
				}
				if (n==2){
				s = sequence(n, s);
				n = next(n);
				System.out.println(s+n);
				}
			}
			count = count + 1;
			n = count;
		}
	}
}

	