from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from .forms import Postform
from app.models import UserPokemon, db

poke_blueprint = Blueprint('poke_blueprint', __name__, template_folder='poke_templates')

@poke_blueprint.route('/posts/create', methods=['GET', 'POST'])
def create_post():
    form = Postform()
    if request.method == 'POST':
        if form.validate():
            name = form.name.data
            ability = form.ability.data
            base_experience = form.base_experience.data
            sprite_url = form.sprite_url.data
            attack_base_stat = form.attack_base_stat.data
            hp_base_stat = form.hp_base_stat.data
            defense_base_stat = form.defense_base_stat.data

            post = UserPokemon(name, ability, base_experience, sprite_url, attack_base_stat, hp_base_stat, defense_base_stat, current_user.id)

            db.session.add(post)
            db.session.commit()
            return redirect(url_for('poke_blueprint.view_posts'))
    return render_template('catch_pokemon.html', form=form)

@poke_blueprint.route('/posts')
def view_posts():
    posts = UserPokemon.query.all()
    return render_template('pokemon_feed.html', posts=posts[::-1])

# my dynamic route for adding who to battle page on battle pages


@poke_blueprint.route('/posts/<int:user_pokemon_id>', methods=['GET', 'POST'])
def view_post(user_pokemon_id):
    globpost = UserPokemon.query.get(user_pokemon_id)
    if globpost:
        global pokeid_integer
        pokeid_integer = int(user_pokemon_id)
        return render_template('battle.html', pokeid_integer=pokeid_integer, globpost=globpost)
    else:
        return redirect(url_for('poke_blueprint.view_posts'))

pokeid_integer = 0

@poke_blueprint.route('/posts2/<int:user_pokemon_id>', methods=['GET', 'POST'])
def battle2_post(user_pokemon_id):
    post2 = UserPokemon.query.get(user_pokemon_id)
    globpost = UserPokemon.query.get(pokeid_integer)
    if post2:
        return render_template('battle2.html', post2=post2, globpost=globpost)
    else:
        return redirect(url_for('poke_blueprint.view_posts'))


# my dynamic route for updating  pokemon
@poke_blueprint.route('/posts/update/<int:user_pokemon_id>', methods=['GET', 'POST'])
def update_card(user_pokemon_id):
    form = Postform()
    post = UserPokemon.query.get(user_pokemon_id)
    if request.method == 'POST':
        if form.validate():
            name = form.name.data
            ability = form.ability.data
            base_experience = form.base_experience.data
            sprite_url = form.sprite_url.data
            attack_base_stat = form.attack_base_stat.data
            hp_base_stat = form.hp_base_stat.data
            defense_base_stat = form.defense_base_stat.data

            post.name = name
            post.ability = ability
            post.base_experience = base_experience
            post.sprite_url = sprite_url
            post.attack_base_stat = attack_base_stat
            post.hp_base_stat = hp_base_stat
            post.defense_base_stat = defense_base_stat

            db.session.commit()
            return redirect(url_for('poke_blueprint.view_posts'))

    return render_template('update_pokecard.html', form=form, post=post)

@poke_blueprint.route('/your_pokemon_collection', methods=['GET','POST'])
def your_deck():
    posts = current_user.user_pokemon
    return render_template('your_pokemon_collection.html', posts = posts)

@poke_blueprint.route('/posts/delete/<int:user_pokemon_id>')
def delete_post(user_pokemon_id):
    post = UserPokemon.query.get(user_pokemon_id)
    if post:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('poke_blueprint.your_deck'))

