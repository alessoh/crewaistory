from vpython import sphere, vector, rate, color, canvas, mag, norm
from math import sin, cos, pi
import random

# Set up the 3D scene
scene = canvas(title='Bouncing Balls in a Sphere', width=800, height=600)

# Parameters for the container and balls
container_radius = 5
ball_radius = 0.2
num_balls = 20

# Create the container sphere (transparent)
container = sphere(pos=vector(0, 0, 0), radius=container_radius, 
                   opacity=0.2, color=color.white)

# Create a list to store the ball objects
balls = []

# Initialize each ball with random position, velocity, and color
for _ in range(num_balls):
    # Random spherical coordinates for a position well inside the container
    r = random.uniform(0, container_radius - ball_radius)
    theta = random.uniform(0, pi)
    phi = random.uniform(0, 2 * pi)
    x = r * sin(theta) * cos(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(theta)
    pos = vector(x, y, z)
    
    # Random speed and direction for velocity
    speed = random.uniform(1, 3)
    theta_v = random.uniform(0, pi)
    phi_v = random.uniform(0, 2 * pi)
    vx = speed * sin(theta_v) * cos(phi_v)
    vy = speed * sin(theta_v) * sin(phi_v)
    vz = speed * cos(theta_v)
    vel = vector(vx, vy, vz)
    
    # Generate a random color using RGB components between 0 and 1
    ball_color = vector(random.random(), random.random(), random.random())
    
    # Create the ball and store its velocity as an attribute
    ball = sphere(pos=pos, radius=ball_radius, color=ball_color, make_trail=False)
    ball.velocity = vel
    balls.append(ball)

# Time step for the simulation
dt = 0.005

# Main simulation loop
while True:
    rate(200)  # Limit the simulation to 200 updates per second
    for ball in balls:
        # Update ball position
        ball.pos = ball.pos + ball.velocity * dt
        
        # Check for collision with the container wall:
        # If the ball is about to exit the sphere, reflect its velocity.
        if mag(ball.pos) + ball.radius > container_radius:
            # Calculate the outward normal vector at the collision point.
            normal = norm(ball.pos)
            # Reflect the velocity: v' = v - 2*(v•n)*n.
            ball.velocity = ball.velocity - 2 * (ball.velocity.dot(normal)) * normal
            # Reset the ball's position to just inside the container to avoid sticking.
            ball.pos = normal * (container_radius - ball.radius)
