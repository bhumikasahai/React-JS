import javax.swing.*;
import java.awt.*;

public class LiangBarskyGUI extends JPanel {
    // Clipping rectangle boundaries
    static final int xmin = 100, ymin = 100, xmax = 300, ymax = 200;

    // Original line endpoints
    double x1 = 50, y1 = 150, x2 = 350, y2 = 180;

    // Clipped line endpoints
    double cx1, cy1, cx2, cy2;
    boolean accept = false;

    public LiangBarskyGUI() {
        liangBarskyClip();
    }

    void liangBarskyClip() {
        double dx = x2 - x1;
        double dy = y2 - y1;

        double[] p = {-dx, dx, -dy, dy};
        double[] q = {x1 - xmin, xmax - x1, y1 - ymin, ymax - y1};

        double u1 = 0.0, u2 = 1.0;

        for (int i = 0; i < 4; i++) {
            if (p[i] == 0) {
                if (q[i] < 0) return; // Line is parallel and outside
            } else {
                double r = q[i] / p[i];
                if (p[i] < 0) {
                    u1 = Math.max(u1, r);
                } else {
                    u2 = Math.min(u2, r);
                }
            }
        }

        if (u1 > u2) return; // No visible portion

        // Line is visible between u1 and u2
        accept = true;
        cx1 = x1 + u1 * dx;
        cy1 = y1 + u1 * dy;
        cx2 = x1 + u2 * dx;
        cy2 = y1 + u2 * dy;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Draw clipping rectangle
        g.setColor(Color.BLACK);
        g.drawRect(xmin, ymin, xmax - xmin, ymax - ymin);

        // Draw original line in RED
        g.setColor(Color.RED);
        g.drawLine((int) x1, (int) y1, (int) x2, (int) y2);

        // Draw clipped line in GREEN
        if (accept) {
            g.setColor(Color.GREEN);
            g.drawLine((int) cx1, (int) cy1, (int) cx2, (int) cy2);
        } else {
            g.setColor(Color.BLUE);
            g.drawString("Line is completely outside the window", 100, 80);
        }
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Liang-Barsky Line Clipping - Java Swing");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);
        frame.add(new LiangBarskyGUI());
        frame.setVisible(true);
    }
}
