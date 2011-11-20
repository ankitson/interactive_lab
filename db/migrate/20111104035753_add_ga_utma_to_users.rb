class AddGaUtmaToUsers < ActiveRecord::Migration
  def self.up
    add_column :users, :ga_utma, :string
  end

  def self.down
    remove_column :users, :ga_utma
  end
end
