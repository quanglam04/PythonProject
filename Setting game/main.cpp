#include <GL/glfw3.h>
#include <iostream>
#include <fstream>

void getScreenResolution(int &width, int &height) {
    glfwInit();
    GLFWwindow* window = glfwCreateWindow(1, 1, "Dummy Window", nullptr, nullptr);
    if (!window) {
        std::cerr << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return;
    }

    // Get the screen size
    const GLFWvidmode* mode = glfwGetVideoMode(glfwGetPrimaryMonitor());
    width = mode->width;
    height = mode->height;

    // Clean up
    glfwDestroyWindow(window);
    glfwTerminate();
}

void writeResolutionToFile(int width, int height) {
    std::ofstream outFile("screen_resolution.txt");
    if (outFile.is_open()) {
        outFile << "Screen Resolution: " << width << "x" << height << std::endl;
        outFile.close();
        std::cout << "Resolution written to screen_resolution.txt" << std::endl;
    } else {
        std::cerr << "Unable to open file for writing." << std::endl;
    }
}

int main() {
    int width, height;
    getScreenResolution(width, height);
    writeResolutionToFile(width, height);
    return 0;
}