import javax.swing.*;
import java.awt.*;

public class ChristmasTree extends JPanel {

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        setBackground(Color.BLUE);

        Graphics2D g2d = (Graphics2D) g;

        
        g2d.setColor(Color.GREEN);
        int[] x1 = {200, 300, 100};
        int[] y1 = {100, 250, 250};
        g2d.fillPolygon(x1, y1, 3);

        int[] x2 = {200, 280, 120};
        int[] y2 = {150, 320, 320};
        g2d.fillPolygon(x2, y2, 3);

        int[] x3 = {200, 260, 140};
        int[] y3 = {200, 380, 380};
        g2d.fillPolygon(x3, y3, 3);

        
        g2d.setColor(new Color(139, 69, 19)); // Brown color
        g2d.fillRect(170, 380, 60, 80);

        
        g2d.setColor(Color.YELLOW);
        g2d.fillOval(190, 80, 20, 20);

        
        g2d.setColor(Color.RED);
        g2d.fillOval(180, 200, 10, 10);
        g2d.fillOval(220, 240, 10, 10);
        g2d.setColor(Color.WHITE);
        g2d.fillOval(160, 260, 10, 10);
        g2d.setColor(Color.ORANGE);
        g2d.fillOval(240, 300, 10, 10);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Christmas Tree");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 500);
        frame.setContentPane(new ChristmasTree());
        frame.setVisible(true);
    }
}