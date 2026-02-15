// Modern vanilla JavaScript - no jQuery needed

// Toggle visibility of element
function togglehide(elemId) {
  const elem = document.getElementById(elemId);
  if (!elem) return;
  
  elem.style.display = elem.style.display === 'none' ? 'block' : 'none';
}

// Smooth scroll to anchor (for Projects link)
document.addEventListener('DOMContentLoaded', () => {
  const links = document.querySelectorAll('a[href^="#"]');
  
  links.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (href === '#') return;
      
      e.preventDefault();
      const target = document.querySelector(href);
      
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
});

// Gallery: Simple image lazy loading hint
if ('loading' in HTMLImageElement.prototype) {
  const images = document.querySelectorAll('img.lazy');
  images.forEach(img => {
    img.src = img.dataset.src;
  });
}

// Advanced Tag Visualization - Physics-based Force Simulation
document.addEventListener('DOMContentLoaded', () => {
  const canvas = document.getElementById('tag-canvas');
  if (!canvas || typeof tagData === 'undefined') return;
  
  const container = document.getElementById('tag-visualization');
  const rect = container.getBoundingClientRect();
  
  canvas.width = rect.width;
  canvas.height = 500;
  
  const ctx = canvas.getContext('2d');
  const width = canvas.width;
  const height = canvas.height;
  
  // Physics parameters - Enhanced for better simulation
  const physics = {
    centerForce: 0.015,
    repelForce: 800,
    linkStrength: 0.02,
    linkDistance: 100,
    damping: 0.88,
    minRadius: 12,
    maxRadius: 45,
    dragDamping: 0.3
  };
  
  // Find max count for log scaling
  const maxCount = Math.max(...tagData.nodes.map(n => n.count));
  const minCount = Math.min(...tagData.nodes.map(n => n.count));
  
  // Initialize nodes with physics properties
  const nodes = tagData.nodes.map(n => {
    // Use logarithmic scale for better visual distribution
    const logScale = Math.log(n.count + 1) / Math.log(maxCount + 1);
    const radius = physics.minRadius + logScale * (physics.maxRadius - physics.minRadius);
    
    return {
      id: n.id,
      count: n.count,
      radius: radius,
      x: width / 2 + (Math.random() - 0.5) * width * 0.3,
      y: height / 2 + (Math.random() - 0.5) * height * 0.3,
      vx: 0,
      vy: 0,
      fx: null, // Fixed position when dragging
      fy: null,
      hovered: false,
      highlighted: false,
      opacity: 1.0
    };
  });
  
  const links = tagData.links;
  
  // Find max link weight for scaling
  const maxWeight = Math.max(...links.map(l => l.weight), 1);
  
  // Build adjacency map for highlighting
  const adjacency = new Map();
  nodes.forEach(n => adjacency.set(n.id, new Set()));
  links.forEach(link => {
    adjacency.get(link.source).add(link.target);
    adjacency.get(link.target).add(link.source);
  });
  
  // Build node map for quick lookup
  const nodeMap = new Map(nodes.map(n => [n.id, n]));
  
  // Mouse and drag state
  let mouseX = 0;
  let mouseY = 0;
  let hoveredNode = null;
  let draggedNode = null;
  let isDragging = false;
  
  // Update hover state
  function updateHover(x, y) {
    hoveredNode = null;
    
    for (const node of nodes) {
      const dx = x - node.x;
      const dy = y - node.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      node.hovered = dist < node.radius + 5;
      if (node.hovered) hoveredNode = node;
    }
    
    // Update highlighting based on hover
    if (hoveredNode) {
      const connectedIds = adjacency.get(hoveredNode.id);
      nodes.forEach(n => {
        n.highlighted = (n === hoveredNode) || connectedIds.has(n.id);
        n.opacity = n.highlighted ? 1.0 : 0.3;
      });
    } else {
      nodes.forEach(n => {
        n.highlighted = false;
        n.opacity = 1.0;
      });
    }
  }
  
  // Mouse event handlers
  canvas.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    mouseX = e.clientX - rect.left;
    mouseY = e.clientY - rect.top;
    
    if (isDragging && draggedNode) {
      draggedNode.fx = mouseX;
      draggedNode.fy = mouseY;
      draggedNode.vx = 0;
      draggedNode.vy = 0;
    } else {
      updateHover(mouseX, mouseY);
    }
    
    canvas.style.cursor = (hoveredNode || isDragging) ? 'pointer' : 'default';
  });
  
  canvas.addEventListener('mousedown', (e) => {
    if (hoveredNode) {
      isDragging = true;
      draggedNode = hoveredNode;
      draggedNode.fx = mouseX;
      draggedNode.fy = mouseY;
      e.preventDefault();
    }
  });
  
  canvas.addEventListener('mouseup', () => {
    if (isDragging && draggedNode && !hoveredNode) {
      // Click without drag - navigate
      window.location.href = `/articles/?tags=${draggedNode.id}`;
    }
    
    if (draggedNode) {
      draggedNode.fx = null;
      draggedNode.fy = null;
    }
    isDragging = false;
    draggedNode = null;
  });
  
  canvas.addEventListener('mouseleave', () => {
    if (draggedNode) {
      draggedNode.fx = null;
      draggedNode.fy = null;
    }
    isDragging = false;
    draggedNode = null;
    updateHover(-1000, -1000); // Clear hover
  });
  
  canvas.addEventListener('click', (e) => {
    if (!isDragging && hoveredNode) {
      window.location.href = `/articles/?tags=${hoveredNode.id}`;
    }
  });
  
  // Physics simulation
  function simulate() {
    // Apply forces to each node
    for (const node of nodes) {
      // Skip if dragging
      if (node.fx !== null && node.fy !== null) {
        node.x = node.fx;
        node.y = node.fy;
        node.vx *= physics.dragDamping;
        node.vy *= physics.dragDamping;
        continue;
      }
      
      // Center gravity
      const dx = width / 2 - node.x;
      const dy = height / 2 - node.y;
      node.vx += dx * physics.centerForce;
      node.vy += dy * physics.centerForce;
      
      // Node repulsion (all pairs)
      for (const other of nodes) {
        if (node === other) continue;
        
        const dx = node.x - other.x;
        const dy = node.y - other.y;
        const distSq = dx * dx + dy * dy;
        const dist = Math.sqrt(distSq) + 0.1;
        
        // Stronger repulsion for closer nodes
        const minDist = node.radius + other.radius + 10;
        const force = physics.repelForce * (node.radius + other.radius) / distSq;
        
        node.vx += (dx / dist) * force;
        node.vy += (dy / dist) * force;
      }
    }
    
    // Link forces (spring attraction between connected nodes)
    for (const link of links) {
      const source = nodeMap.get(link.source);
      const target = nodeMap.get(link.target);
      if (!source || !target) continue;
      
      const dx = target.x - source.x;
      const dy = target.y - source.y;
      const dist = Math.sqrt(dx * dx + dy * dy) + 0.1;
      
      // Spring force pulls connected nodes together
      const idealDist = physics.linkDistance * (1 - link.weight / maxWeight * 0.3);
      const force = (dist - idealDist) * physics.linkStrength * Math.sqrt(link.weight);
      
      const fx = (dx / dist) * force;
      const fy = (dy / dist) * force;
      
      if (source.fx === null) {
        source.vx += fx;
        source.vy += fy;
      }
      if (target.fx === null) {
        target.vx -= fx;
        target.vy -= fy;
      }
    }
    
    // Update positions with velocity and damping
    for (const node of nodes) {
      if (node.fx !== null && node.fy !== null) continue;
      
      // Apply damping
      node.vx *= physics.damping;
      node.vy *= physics.damping;
      
      // Update position
      node.x += node.vx;
      node.y += node.vy;
      
      // Keep in bounds with soft walls
      const margin = node.radius + 5;
      if (node.x < margin) {
        node.x = margin;
        node.vx *= -0.5;
      } else if (node.x > width - margin) {
        node.x = width - margin;
        node.vx *= -0.5;
      }
      
      if (node.y < margin) {
        node.y = margin;
        node.vy *= -0.5;
      } else if (node.y > height - margin) {
        node.y = height - margin;
        node.vy *= -0.5;
      }
    }
  }
  
  // Render
  function render() {
    ctx.clearRect(0, 0, width, height);
    
    // Draw links with thickness based on weight
    for (const link of links) {
      const source = nodeMap.get(link.source);
      const target = nodeMap.get(link.target);
      if (!source || !target) continue;
      
      // Determine if this link should be highlighted
      const isHighlighted = source.highlighted && target.highlighted;
      
      // Calculate line thickness based on weight (log scale)
      const thickness = 0.5 + Math.log(link.weight + 1) * 1.5;
      
      ctx.beginPath();
      ctx.moveTo(source.x, source.y);
      ctx.lineTo(target.x, target.y);
      
      if (isHighlighted) {
        ctx.strokeStyle = 'rgba(59, 130, 246, 0.6)';
        ctx.lineWidth = thickness * 1.5;
      } else {
        ctx.strokeStyle = `rgba(100, 100, 100, ${0.15 * source.opacity * target.opacity})`;
        ctx.lineWidth = thickness;
      }
      
      ctx.stroke();
    }
    
    // Draw nodes
    for (const node of nodes) {
      ctx.save();
      
      // Node circle
      ctx.beginPath();
      ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
      
      // Calculate opacity and color
      const baseOpacity = node.opacity;
      
      if (node.hovered) {
        // Hovered state - bright blue
        const gradient = ctx.createRadialGradient(
          node.x, node.y, 0,
          node.x, node.y, node.radius
        );
        gradient.addColorStop(0, '#60a5fa');
        gradient.addColorStop(1, '#3b82f6');
        ctx.fillStyle = gradient;
        ctx.fill();
        
        ctx.strokeStyle = '#93c5fd';
        ctx.lineWidth = 3;
        ctx.stroke();
      } else if (node.highlighted) {
        // Highlighted (connected to hovered)
        const gradient = ctx.createRadialGradient(
          node.x, node.y, 0,
          node.x, node.y, node.radius
        );
        gradient.addColorStop(0, `rgba(96, 165, 250, ${baseOpacity})`);
        gradient.addColorStop(1, `rgba(59, 130, 246, ${baseOpacity * 0.8})`);
        ctx.fillStyle = gradient;
        ctx.fill();
        
        ctx.strokeStyle = `rgba(59, 130, 246, ${baseOpacity})`;
        ctx.lineWidth = 2;
        ctx.stroke();
      } else {
        // Normal state
        const gradient = ctx.createRadialGradient(
          node.x, node.y, 0,
          node.x, node.y, node.radius
        );
        gradient.addColorStop(0, `rgba(59, 130, 246, ${baseOpacity * 0.7})`);
        gradient.addColorStop(1, `rgba(30, 64, 175, ${baseOpacity * 0.5})`);
        ctx.fillStyle = gradient;
        ctx.fill();
        
        ctx.strokeStyle = `rgba(59, 130, 246, ${baseOpacity * 0.6})`;
        ctx.lineWidth = 1.5;
        ctx.stroke();
      }
      
      // Draw label - size proportional to node size
      const fontSize = Math.max(10, Math.min(14, node.radius * 0.55));
      ctx.font = `${fontSize}px Inter, sans-serif`;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      
      // Add text shadow for better readability
      ctx.shadowColor = 'rgba(0, 0, 0, 0.8)';
      ctx.shadowBlur = 4;
      ctx.shadowOffsetX = 0;
      ctx.shadowOffsetY = 1;
      
      if (node.hovered || node.radius > 18) {
        ctx.fillStyle = `rgba(255, 255, 255, ${baseOpacity})`;
        ctx.fillText(node.id, node.x, node.y);
      }
      
      ctx.restore();
    }
    
    // Draw hover tooltip
    if (hoveredNode && !isDragging) {
      ctx.save();
      
      const text = `${hoveredNode.id} (${hoveredNode.count} article${hoveredNode.count !== 1 ? 's' : ''})`;
      ctx.font = '13px Inter, sans-serif';
      const metrics = ctx.measureText(text);
      const padding = 10;
      const boxWidth = metrics.width + padding * 2;
      const boxHeight = 28;
      const boxX = hoveredNode.x - boxWidth / 2;
      const boxY = hoveredNode.y - hoveredNode.radius - boxHeight - 12;
      
      // Tooltip background
      ctx.fillStyle = 'rgba(17, 17, 17, 0.95)';
      ctx.strokeStyle = '#3b82f6';
      ctx.lineWidth = 2;
      
      ctx.beginPath();
      ctx.roundRect(boxX, boxY, boxWidth, boxHeight, 6);
      ctx.fill();
      ctx.stroke();
      
      // Tooltip text
      ctx.fillStyle = '#ffffff';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.shadowColor = 'transparent';
      ctx.fillText(text, hoveredNode.x, boxY + boxHeight / 2);
      
      ctx.restore();
    }
  }
  
  // Animation loop - 60fps
  let running = true;
  let lastTime = performance.now();
  let iterations = 0;
  const maxIterations = 400; // Run physics for ~6.7 seconds
  
  function animate(currentTime) {
    if (!running) return;
    
    const deltaTime = currentTime - lastTime;
    lastTime = currentTime;
    
    // Run physics simulation
    if (iterations < maxIterations || isDragging) {
      simulate();
      iterations++;
    }
    
    // Always render
    render();
    
    requestAnimationFrame(animate);
  }
  
  // Start animation
  requestAnimationFrame(animate);
  
  // Handle window resize
  let resizeTimeout;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
      const rect = container.getBoundingClientRect();
      canvas.width = rect.width;
      canvas.height = 500;
      // Reset iterations to allow re-settling
      iterations = 0;
    }, 250);
  });
});
