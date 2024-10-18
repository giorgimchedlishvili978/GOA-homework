* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #333;
    padding: 10px 20px;
}

.logo {
    color: white;
    font-size: 24px;
}

.nav-list {
    list-style: none;
    display: flex;
}

.nav-list li {
    margin: 0 15px;
}

.nav-list a {
    color: white;
    text-decoration: none;
    transition: color 0.3s;
}

.nav-list a:hover {
    color: #ff6347; /* ანიმაციის დროს გადადის ლამაზ ფერში */
}

.menu-toggle {
    display: none;
    flex-direction: column;
    cursor: pointer;
}

.menu-toggle .bar {
    height: 3px;
    width: 25px;
    background-color: white;
    margin: 3px 0;
    transition: all 0.3s ease;
}

/* Responsive */
@media (max-width: 768px) {
    .nav-list {
        display: none;
        flex-direction: column;
        width: 100%;
        background-color: #333;
        position: absolute;
        top: 60px;
        left: 0;
        z-index: 1;
        animation: slideDown 0.5s forwards;
    }

    .nav-list.active {
        display: flex;
    }

    .menu-toggle {
        display: flex;
    }

    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
}
