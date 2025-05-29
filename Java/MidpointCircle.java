import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

public class MidpointCircle {

    public static Set<String> plotCirclePoints(int xc, int yc, int x, int y) {
        Set<String> points = new HashSet<>();

        points.add((xc + x) + "," + (yc + y));
        points.add((xc - x) + "," + (yc + y));
        points.add((xc + x) + "," + (yc - y));
        points.add((xc - x) + "," + (yc - y));
        points.add((xc + y) + "," + (yc + x));
        points.add((xc - y) + "," + (yc + x));
        points.add((xc + y) + "," + (yc - x));
        points.add((xc - y) + "," + (yc - x));

        return points;
    }

    public static void midpointCircle(int xc, int yc, int r) {
        int x = 0;
        int y = r;
        int p = 1 - r;
        Set<String> circlePoints = new HashSet<>();

        while (x <= y) {
            circlePoints.addAll(plotCirclePoints(xc, yc, x, y));
            x++;
            if (p < 0) {
                p = p + 2 * x + 1;
            } else {
                y--;
                p = p + 2 * x + 1 - 2 * y;
            }
        }

        // Sort and print
        Set<String> sortedPoints = new TreeSet<>(circlePoints);
        for (String point : sortedPoints) {
            System.out.println("(" + point + ")");
        }
    }

    public static void main(String[] args) {
        midpointCircle(0, 0, 5);
    }
}
