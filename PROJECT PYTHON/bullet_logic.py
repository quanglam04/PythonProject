import pygame
import math


class Laser_logic:
    CORNER_TOLERANCE = 3  # Allowable distance to consider it a corner hit

    def get_normal_vector(self, wall, line):
        """ Helper function to get the normal vector of a wall based on collision point. """
        if abs(line[0][0] - wall.x) <= 1.5:  # Left vertical wall
            return [-1, 0]
        elif abs(line[0][0] - wall.x - wall.width) <= 1.5:  # Right vertical wall
            return [1, 0]
        elif abs(line[0][1] - wall.y) <= 1.5:  # Top horizontal wall
            return [0, -1]
        elif abs(line[0][1] - wall.y - wall.height) <= 1.5:  # Bottom horizontal wall
            return [0, 1]
        return [0, 0]  # Default case, should not happen

    def is_near_corner(self, line_1, line_2):
        """ Helper function to check if two collision points are within the corner tolerance. """
        dx = abs(line_1[0][0] - line_2[0][0])
        dy = abs(line_1[0][1] - line_2[0][1])
        return dx <= self.CORNER_TOLERANCE and dy <= self.CORNER_TOLERANCE

    def cal_end_point(self, collision_map):
        # Calculate end point of the laser bullet
        self.end_x = self.x + self.length * math.cos(math.radians(self.angle))
        self.end_y = self.y - self.length * math.sin(math.radians(self.angle))

        # Check the wall collisions
        self.check = 0  # 0: no collision, 1: hit 1 wall, 2: hit 2 walls (corner)
        collided_lines = []

        # First loop: check which walls the bullet will hit
        for wall in collision_map:
            line = wall.clipline(self.x, self.y, self.end_x, self.end_y)
            if line and (abs(self.x - line[0][0]) > 1.5 and abs(self.y - line[0][1]) > 1.5):
                self.check += 1
                collided_lines.append((wall, line))

        # If no collision
        if self.check == 0:
            return

        # Corner case detection
        if self.check == 2:
            print(2)
            wall_1, line_1 = collided_lines[0]
            wall_2, line_2 = collided_lines[1]

            if self.is_near_corner(line_1, line_2):
                # Handle the corner reflection using combined normals
                normal_1 = self.get_normal_vector(wall_1, line_1)
                normal_2 = self.get_normal_vector(wall_2, line_2)

                combined_normal_x = normal_1[0] + normal_2[0]
                combined_normal_y = normal_1[1] + normal_2[1]

                # Normalize the combined normal
                length = math.sqrt(combined_normal_x ** 2 + combined_normal_y ** 2)
                if length != 0:
                    combined_normal_x /= length
                    combined_normal_y /= length

                # Reflect the direction vector using the combined normal
                dot_product = (self.direction_x * combined_normal_x + self.direction_y * combined_normal_y)
                self.direction_x -= 2 * dot_product * combined_normal_x
                self.direction_y -= 2 * dot_product * combined_normal_y

                # Update the angle based on the new direction
                self.angle = math.degrees(math.atan2(-self.direction_y, self.direction_x)) % 360

                # Set the endpoint to the first collision point (just before hitting the corner)
                self.end_x = line_1[0][0]
                self.end_y = line_1[0][1]

                self.bounces += 1
                return

        # Handle a single wall hit
        if self.check == 1:
            print(1)
            wall, line = collided_lines[0]
            self.end_x = line[0][0]
            self.end_y = line[0][1]

            self.bounces += 1

            normal = self.get_normal_vector(wall, line)

            # Reflect based on normal
            if normal[0] != 0:  # Vertical wall, reflect horizontally
                self.angle = 180 - self.angle
                self.direction_x *= -1
            else:  # Horizontal wall, reflect vertically
                self.angle = 360 - self.angle
                self.direction_y *= -1

    def update(self):
        if self.check != 0:
            # Move the laser based on its new direction after reflection
            self.direction_x = math.cos(math.radians(self.angle)) * self.speed
            self.direction_y = -math.sin(math.radians(self.angle)) * self.speed

            self.x = self.end_x + (self.direction_x * 10)
            self.y = self.end_y + (self.direction_y * 10)
        else:
            # Move laser in the current direction (no reflection yet)
            self.x += self.direction_x
            self.y += self.direction_y

    def is_expired_bullet(self):
        return self.bounces >= 6

class Bullet_logic:
    def cal_end_point(self, collision_map):
        for wall in collision_map:
            if self.rect.colliderect(wall):
                # Handle vertical wall collisions
                if self.rect.right >= wall.left and self.rect.left < wall.left:  # Right wall
                    self.rect.right = wall.left
                    self.direction_x *= -1
                    self.angle = 180 - self.angle

                elif self.rect.left <= wall.right and self.rect.right > wall.right:  # Left wall
                    self.rect.left = wall.right
                    self.direction_x *= -1
                    self.angle = 180 - self.angle

                # Handle horizontal wall collisions
                if self.rect.bottom >= wall.top and self.rect.top < wall.top:  # Bottom wall
                    self.rect.bottom = wall.top
                    self.direction_y *= -1
                    self.angle = 360 - self.angle

                elif self.rect.top <= wall.bottom and self.rect.bottom > wall.bottom:  # Top wall
                    self.rect.top = wall.bottom
                    self.direction_y *= -1
                    self.angle = 360 - self.angle

                # If the bullet collides with both a vertical and a horizontal wall, this will reverse both directions.
                self.bounces += 1
                break  # Exit after processing the first collision

    def update(self):
        # Move the bullet
        self.x += self.direction_
        self.y += self.direction_y
        self.rect.center = (self.x, self.y)  # Update the rectangle's position to match

    def is_expired_bullet(self):
        return self.bounces >= 6  # Expire the bullet after 6 bounces

    def update(self):
        self.x += self.direction_x
        self.y += self.direction_y
        self.rect.center = (self.x, self.y)


    def is_expired_bullet(self):
        return self.bounces >= 6