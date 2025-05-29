import java.awt.*;
import javax.swing.*;
public class DDALineDrawing extends JPanel {
    int x1 = 50, y1 = 50, x2 = 200, y2 = 150;
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        drawLineDDA(g, x1, y1, x2, y2);
    }
    public void drawLineDDA(Graphics g, int x1, int y1, int x2, int y2) {
        int dx = x2 - x1;
        int dy = y2 - y1;
        int steps = Math.max(Math.abs(dx), Math.abs(dy));
        float xInc = dx / (float) steps;
        float yInc = dy / (float) steps;
        float x = x1;
        float y = y1;
        for (int i = 0; i <= steps; i++) {
            g.fillRect(Math.round(x), Math.round(y), 1, 1); 
            x += xInc;
            y += yInc;
        }
    }
    public static void main(String[] args) {
        JFrame frame = new JFrame("DDA Line Drawing");
        DDALineDrawing panel = new DDALineDrawing();
        frame.add(panel);
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
