class CreateFlavornotes < ActiveRecord::Migration[7.0]
  def change
    create_table :flavornotes do |t|
      t.text :content
      t.references :user, null: false, foreign_key: true

      t.timestamps
    end
    add_index :flavornotes, [:user_id, :created_at]
  end
end
