import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;


public class Driver {
	private static Scanner scan = new Scanner(System.in);
	private static Scanner dict;
	

	public static void main(String[] args) throws FileNotFoundException {
		dict = new Scanner(new File("four.txt")); 
		ArrayList<String> dl = new ArrayList<>();
		String temp,start,end,current,again = "";
		boolean found = false;
		boolean flag = true;
		int words = 0;
		String a = "abcdefghijklmnopqrstuvwxyz";
		char[] chars = a.toCharArray();
		
		while(dict.hasNext()){ //reads from file
			dl.add(dict.next());
		}
		
		do{
			start= "";
			end = "";
			
			while(start.length() != 4) {
				System.out.print("\nEnter the starting four letter word: ");
				start = scan.next().toLowerCase();
			}
			
			while(end.length() != 4) {
				System.out.print("\nEnter four letter word you wish to end with: ");
				end = scan.next().toLowerCase();
			}
			
			if (start.equals(end)){
				System.out.print("\nThose were the same words\n");
			}
			else if(!dl.contains(start)){
				System.out.println("\nYour starting word was not valid");
			}
			else if(!dl.contains(end)){
				System.out.println("\nYour ending word was not valid");
			}
			else{ // the part that actually finds the word chain
				System.out.println("\nFinding a word chain between " + start + " and " + end + "\n");
				found = false;
				words = 0;
				ArrayList<String> used = new ArrayList<>();
				ArrayList<String> next = new ArrayList<>();
				LinearNode<String> startn = new LinearNode<String>();
				LinearNode<String> currentn = new LinearNode<String>();
				LinearNode<String> endn = new LinearNode<String>();
				LinkedQueue<LinearNode<String>> poss = new LinkedQueue<>();
				Stack<String> wc = new Stack<>();
				
				used.add(start);
				startn.setElement(start);
				poss.enqueue(startn);
				
				while(!found && !poss.isEmpty()){
					currentn = poss.dequeue();
					current = currentn.getElement();
					StringBuilder sb = new StringBuilder(current);
					temp = current;
				
					for(int i = 0;i < current.length();i++){
						for (char c : chars){
							sb.setCharAt(i,c);
							temp = sb.toString();
							
							if (dl.contains(temp) && !used.contains(temp)){
								next.add(temp);
								used.add(temp);
								LinearNode<String> neww = new LinearNode<String>();
								neww.setElement(temp);
								neww.setNext(currentn);
								poss.enqueue(neww);
								
								if (temp.equals(end)){
									endn.setNext(neww);
									found = true;
								}
								else 
									found = false;
							}
						}
						sb = new StringBuilder(current);
					}
				}
				while(endn.getNext() != null){
					endn = endn.getNext();
					wc.push(endn.getElement());
				}
				words = 0;
				while (!wc.isEmpty()){ // shows the words in the chain and keeps count
					System.out.println(wc.pop());
					words++;
				}
				if (words == 0){
					System.out.println("\nI'm sorry, no wordchain was found.");
				}
				if (words !=0){  //only prints if there is a word chain
				System.out.println("\nThis is a chain of " + words + " words");
				}
			}
			
			flag = true;
			while (flag){ // allows user to run it again
				again = "";
				System.out.println("\nAgain? (Y or N)");
				again = scan.next().toLowerCase();
				if(again.equals("y") || again.equals("n"))
					flag = false;
			}	
		}while (again.toLowerCase().equals("y"));
	}

	
}