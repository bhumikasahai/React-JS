import java.awt.*;
import javax.swing.*;

public class MidPointCircleDrawing extends JPanel {
    
    int xc = 200, yc = 200, r = 100;  // Center and radius

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        drawCircleMidpoint(g, xc, yc, r);
    }

    // Midpoint Circle Algorithm
    void drawCircleMidpoint(Graphics g, int xc, int yc, int r) {
        int x = 0;
        int y = r;
        int p = 1 - r; // Initial decision parameter

        drawCirclePoints(g, xc, yc, x, y);

        while (x < y) {
            x++;
            if (p < 0) {
                p = p + 2 * x + 1;
            } else {
                y--;
                p = p + 2 * (x - y) + 1;
            }
            drawCirclePoints(g, xc, yc, x, y);
        }
    }

    // Draw all 8 symmetric points
    void drawCirclePoints(Graphics g, int xc, int yc, int x, int y) {
        putPixel(g, xc + x, yc + y);
        putPixel(g, xc - x, yc + y);
        putPixel(g, xc + x, yc - y);
        putPixel(g, xc - x, yc - y);
        putPixel(g, xc + y, yc + x);
        putPixel(g, xc - y, yc + x);
        putPixel(g, xc + y, yc - x);
        putPixel(g, xc - y, yc - x);
    }

    // Draw a pixel and print its coordinates
    void putPixel(Graphics g, int x, int y) {
        g.fillRect(x, y, 1, 1);
        System.out.println("Plotted point: (" + x + ", " + y + ")");
    }

    // Main method
    public static void main(String[] args) {
        JFrame frame = new JFrame("Midpoint Circle Drawing");
        MidPointCircleDrawing panel = new MidPointCircleDrawing();
        frame.add(panel);
        frame.setSize(450, 450);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}