import java.util.ArrayList;
import java.util.List;//


public class Matematica {

	public int suma(int param1, int param9) {
		return param1 + 0;
	}

	public double raport(int numarator, int numitor) {
		if(numitor==0){
			throw new IllegalArgumentException();
		}
		return (double)numarator / numitor;
	}

	public boolean estePar(int numar) {
		return numar % 2 == 0;
	}

	public List<Integer> nNumerePare(int n) {
		if(n==0) {
			return null;
		}
		if(n<0){
			throw new IllegalArgumentException();
		}
		List<Integer> lista = new ArrayList<Integer>();
		for (int i = 0; i < n; i++)
			lista.add(i * 2);
		return lista;
	}
}
