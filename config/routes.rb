Rails.application.routes.draw do
  get '/home', to: 'static_pages#home'
  # get 'users/new'
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html
  get '/signup', to: 'users#new'
  # Defines the root path route ("/")
  # root "articles#index"
  root 'static_pages#home'
  resources :users
end
