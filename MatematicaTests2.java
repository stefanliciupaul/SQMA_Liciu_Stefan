import static org.junit.Assert.*;
import java.util.List;
import org.junit.Before; 
import org.junit.Test;

public class MatematicaTests2 {
	Matematica mate;
	
	@Before
	public void setUp(){
		mate=new Matematica();
	}
	
	@Test
	public void testSumaCorectitudine() {
		int rezultat=mate.suma(3, 12);
		int rezultatAsteptat=15;
		assertEquals(rezultatAsteptat, rezultat);
	}
	
	
	@Test
	public void testEsteParCorect(){
		assertTrue(mate.estePar(8));
		assertFalse(mate.estePar(9));
		assertFalse(mate.estePar(-9));
	}
	
	
	@Test
	public void testNNumerePareDimensiune(){
		int nrElemente=8;
		List<Integer> lista=mate.nNumerePare(nrElemente);
		assertEquals(nrElemente, lista.size());
	}
	
	@Test
	public void testNNumerePareNULL(){
		List<Integer> lista=mate.nNumerePare(0);
		assertNull(lista);
	}
	
	@Test(expected=IllegalArgumentException.class)
	public void testNNumerePareNumarNegativ(){
		List<Integer> lista=mate.nNumerePare(-2);

	}
}
