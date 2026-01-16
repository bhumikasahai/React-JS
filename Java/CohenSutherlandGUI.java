import javax.swing.*;
import java.awt.*;

public class CohenSutherlandGUI extends JPanel {
    // Region codes
    static final int INSIDE = 0; // 0000
    static final int LEFT = 1;   // 0001
    static final int RIGHT = 2;  // 0010
    static final int BOTTOM = 4; // 0100
    static final int TOP = 8;    // 1000

    // Clipping window
    static final int xmin = 100, ymin = 100, xmax = 300, ymax = 200;

    // Original line coordinates
    double x1 = 50, y1 = 150, x2 = 350, y2 = 150;

    // Clipped line coordinates
    double cx1, cy1, cx2, cy2;
    boolean accept = false;

    public CohenSutherlandGUI() {
        // Perform clipping during initialization
        cohenSutherlandClip();
    }

    int computeCode(double x, double y) {
        int code = INSIDE;

        if (x < xmin) code |= LEFT;
        else if (x > xmax) code |= RIGHT;
        if (y < ymin) code |= BOTTOM;
        else if (y > ymax) code |= TOP;

        return code;
    }

    void cohenSutherlandClip() {
        double x1 = this.x1, y1 = this.y1, x2 = this.x2, y2 = this.y2;
        int code1 = computeCode(x1, y1);
        int code2 = computeCode(x2, y2);
        boolean done = false;

        while (!done) {
            if ((code1 | code2) == 0) {
                // Both points inside
                accept = true;
                done = true;
            } else if ((code1 & code2) != 0) {
                // Line is completely outside
                done = true;
            } else {
                int codeOut = (code1 != 0) ? code1 : code2;
                double x = 0, y = 0;

                if ((codeOut & TOP) != 0) {
                    x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1);
                    y = ymax;
                } else if ((codeOut & BOTTOM) != 0) {
                    x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1);
                    y = ymin;
                } else if ((codeOut & RIGHT) != 0) {
                    y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1);
                    x = xmax;
                } else if ((codeOut & LEFT) != 0) {
                    y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1);
                    x = xmin;
                }

                if (codeOut == code1) {
                    x1 = x;
                    y1 = y;
                    code1 = computeCode(x1, y1);
                } else {
                    x2 = x;
                    y2 = y;
                    code2 = computeCode(x2, y2);
                }
            }
        }

        if (accept) {
            cx1 = x1;
            cy1 = y1;
            cx2 = x2;
            cy2 = y2;
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Draw clipping rectangle
        g.setColor(Color.BLACK);
        g.drawRect(xmin, ymin, xmax - xmin, ymax - ymin);

        // Draw original line in red
        g.setColor(Color.RED);
        g.drawLine((int) x1, (int) y1, (int) x2, (int) y2);

        // Draw clipped line in green
        if (accept) {
            g.setColor(Color.GREEN);
            g.drawLine((int) cx1, (int) cy1, (int) cx2, (int) cy2);
        } else {
            g.setColor(Color.BLUE);
            g.drawString("Line is completely outside the window", 100, 80);
        }
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Cohen-Sutherland Line Clipping - Java Swing");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);
        frame.add(new CohenSutherlandGUI());
        frame.setVisible(true);
    }
}
