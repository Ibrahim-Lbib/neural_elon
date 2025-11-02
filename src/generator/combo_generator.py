# offline/random-combo logic
import random
import os

industries = [
    "transportation", "education", "energy", "medicine", "space", "AI", "agriculture",
    "finance", "construction", "manufacturing", "telecommunication", "mining",
    "entertainment", "defense", "biotech", "genetics", "retail", "real estate",
    "climate tech", "water management", "robotics", "nanotech", "food production",
    "clean tech", "waste management", "ocean exploration", "cybersecurity",
    "logistics", "autonomous systems", "smart cities", "satellite communication",
    "virtual reality", "augmented reality", "metaverse", "insurance", "supply chain",
    "governance", "sports science", "aerospace", "materials science",
    "space mining", "healthcare", "bioinformatics", "neuroscience", "transport hubs"
]

techs = [
    "quantum", "AI-powered", "solar", "autonomous", "blockchain", "neural",
    "drone-based", "fusion", "biometric", "genetic", "holographic", "cybernetic",
    "5G", "6G", "nano-engineered", "bio-hybrid", "quantum-encrypted", "hydrogen",
    "decentralized", "synthetic", "cloud-based", "self-repairing", "hyperloop",
    "smart", "predictive", "swarm", "edge-computing", "anti-gravity", "cryogenic",
    "geoengineering", "robotic", "AI-augmented", "adaptive", "liquid metal",
    "zero-emission", "eco-reactive", "bio-computational", "voice-controlled",
    "brain-linked", "fusion-driven", "quantum-optimized", "solar-thermal"
]

concepts = [
    "platform", "network", "device", "service", "ecosystem", "infrastructure", "colony",
    "marketplace", "protocol", "engine", "framework", "hub", "assistant", "system",
    "market", "interface", "station", "vehicle", "framework", "OS", "datacenter",
    "colony", "habitat", "AI agent", "microgrid", "app", "virtual world",
    "toolkit", "factory", "platform-as-a-service", "network-as-a-service",
    "accelerator", "processor", "server", "wearable", "implant", "drone fleet",
    "simulation", "metaverse layer", "grid", "market engine", "fusion plant"
]

goals = [
    "eliminate poverty", "make Mars livable", "remove human error", "extend life", "build faster cities",
    "end traffic congestion", "decarbonize the planet", "connect all humans", "make energy free",
    "colonize other planets", "reverse climate change", "cure all diseases", "automate everything",
    "extend human intelligence", "replace fossil fuels", "clean all oceans", "preserve biodiversity",
    "rebuild ecosystems", "achieve world peace", "make education universal", "create self-sustaining cities",
    "make food abundant", "make work optional", "end corruption", "achieve global equality",
    "digitize consciousness", "merge humans and AI", "stop aging", "recycle 100% waste",
    "connect human brains", "eliminate pollution", "enable instant travel", "terraform other worlds",
    "achieve full automation", "restore forests", "democratize innovation", "achieve energy independence",
    "map the human brain", "simulate reality", "reach interstellar travel"
]
def generate_startup_idea():
    industry = random.choice(industries)
    tech = random.choice(techs)
    concept = random.choice(concepts)
    goal = random.choice(goals)
    
    idea = f"A {tech} {concept} in the {industry} industry that aims to {goal}."
    return idea